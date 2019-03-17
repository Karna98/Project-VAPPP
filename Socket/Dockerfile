FROM node:10

WORKDIR usr/src/app

COPY package.json ./

RUN npm install

RUN npm install --save express

RUN npm install http
RUN npm install ejs

RUN npm install express-ejs-layouts

RUN npm install mongoose
RUN npm install body-parser

RUN npm install socket.io
RUN npm install cors




COPY . .

EXPOSE 3000

CMD ["npm","start"]
