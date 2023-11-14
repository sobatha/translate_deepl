FROM node:18.17.1

WORKDIR /app

# COPY . /app

# RUN npm install

CMD ["npm", "run", "dev", "--", "--host"]
