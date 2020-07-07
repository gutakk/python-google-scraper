FROM node:14

# add `/app/node_modules/.bin` to $PATH
ENV PATH /web/node_modules/.bin:$PATH

COPY ./web /web

WORKDIR /web

RUN npm install

EXPOSE 3000
# start app
CMD ["npm", "start"]