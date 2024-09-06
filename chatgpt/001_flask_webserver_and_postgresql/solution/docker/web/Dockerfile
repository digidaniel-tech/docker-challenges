# syntax=docker/dockerfile:1.4

# 1. For build React app
FROM node:lts AS development

# Set working directory
WORKDIR /app

# 
COPY ./web/package.json /app/package.json
COPY ./web/package-lock.json /app/package-lock.json

# Same as npm install
RUN npm ci

COPY ./web /app

ENV CI=true
ENV PORT=3000

RUN npm run build

CMD [ "npm", "start" ]