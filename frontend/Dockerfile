FROM node:22.8-alpine3.19

WORKDIR /app

COPY package.json /app/
COPY package-lock.json /app/


RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000

CMD [ "npm", "run", "dev" ]