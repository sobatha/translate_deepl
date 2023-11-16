FROM node:18.17.1

WORKDIR /app

COPY ./package.json /app/package.json

# RUN npm install

CMD ["npm", "run", "dev", "--", "--host"]
