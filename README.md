# draw-something

It is the draw-something Application. Front-End is built with `webpack` + `Vue.js` + `Vuex` + `Vue-Router` + `Muse-UI`, and Back-End will be build with `Node.js` and `Python3`.

[中文文档](./README_ZH.md)


Enter GitHub to see [code](https://github.com/xingbofeng/vue-draw-something)!

## Technology stack
### Front-End
- `vue` + `vuex`+ `vue-router` vue based project
- `webpack` + `webpack-dev-server` + `http-proxy-middleware` dev environment we use webpack-dev-server and http-proxy-middleware.
- `Muse-UI` UI components library
- `yarn` package manager.

### Back-End
#### Node.js
- `Express` + `http-proxy-middleware` online we use Express and http-proxy-middleware
- `socket.io`
- `postman` test our interface.
#### Python
- `Python3`
- `Flask`

## Online

敬请期待

## Development

Warning: If you are a developer of `Python`, you should update the version of your `Python`, this project is only supported `Python3.x`.

If you are a developer of `Node.js`, this project is based on `es5` :smile:!Without any grammar of `es6`, it can run Lower version of `Node.js`.


```
git clone https://github.com/xingbofeng/vue-draw-something.git

cd vue-draw-something

yarn install

yarn run node / yarn run python
```

Then open your browser, and go to http://localhost:8080/ to enjoy it!

## Preview

敬请期待

## Functions

敬请期待

## Directory
```
|
|—— build 
|—— config
|
|——src : dev resources.
|   |—— server/ : The Back-End with `Python3` or `Node.js`
|   |      |—— Node/ : The Back-End with `Node.js`
|   |      |__ Python/ : The Back-End with `Python`
|   |__ client/ : The Front-End with `Vue.js`
|          |—— assets : images
|          |—— components/
|          |    |____ Common/ : reusable components
|          |    |____ ... : other components of the own page.
|          |
|          |—— router/
|          |    |____ index.js : the entry of router.
|          |    |____ server.js : export ajax function.
|          |    |____ serverConfig.js : export the server detail.
|          |    |____ routes/ : every page's router, changing the state of `vuex` at its lifecycle function.
|          |
|          |—— store : vuex
|          |—— App.vue : vue-draw-something
|          |__ main.js : the entry of vue-draw-something
|
|__ static : static files

```

## Support

Thanks for you support,being glad for your `star`, `pr`, `follow` and `issue`.

When you see bugs.You can mail to me! me@xingbofeng.com !
