FROM python:3.11
 
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    curl \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libatspi2.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libu2f-udev \
    libvulkan1 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxkbcommon0 \
    libxrandr2 \
    xdg-utils \
    && rm -rf /var/lib/apt/lists/*
 
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get install -y ./google-chrome-stable_current_amd64.deb \
    && rm -rf /var/lib/apt/lists/*
 
ARG CHROMEDRIVER_VERSION="latest"
RUN if [ "$CHROMEDRIVER_VERSION" = "latest" ]; then \
        CHROMEDRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"); \
    fi \
    # && CHROMEDRIVER_URL="https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip" \
    && CHROMEDRIVER_URL="https://storage.googleapis.com/chrome-for-testing-public/124.0.6367.91/linux64/chromedriver-linux64.zip" \
    && wget -q "$CHROMEDRIVER_URL" -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d /tmp/ \
    && mv /tmp/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver \
    && rm /tmp/chromedriver.zip \
    && chmod +x /usr/local/bin/chromedriver

WORKDIR /app
 
COPY requirements.txt .
 
RUN pip install --no-cache-dir -r requirements.txt

COPY chrome-wrapper.sh /opt/bin/wrap_chrome_binary
RUN /opt/bin/wrap_chrome_binary

COPY . .

CMD ["behave"]