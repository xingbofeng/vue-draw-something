# draw-something

It is the draw-something Application. Front-End is built with `webpack` + `Vue.js` + `Vuex` + `Vue-Router` + `Muse-UI`, and Back-End will be build with `Node.js` and `Python3`.

[中文文档](./README_ZH.md)


Enter GitHub to see [code](https://github.com/xingbofeng/vue-draw-something)!

Thanks for you support, waiting for your `issue`, `pr`, `star` or `follow`!I will release more interesting project in the future!

## Online

(敬请期待)

Or you can clone this project to you own local environment, then enjoy this project online：

```
git clone https://github.com/xingbofeng/vue-draw-something.git

cd vue-draw-something

yarn install

yarn run serve
```

Then open your browser, and go to http://localhost:8080/ to enjoy it!

## Development
```
git clone https://github.com/xingbofeng/vue-draw-something.git

cd vue-draw-something

yarn install

yarn run serve
```

Then open your browser, and go to http://localhost:8080/ to enjoy it!

## Preview

敬请期待

## Technology stack
- `vue` + `vuex`+ `vue-router` vue based project
- `webpack` + `webpack-dev-server` + `http-proxy-middleware` dev environment we use webpack-dev-server and http-proxy-middleware.
- `express` + `http-proxy-middleware` online we use express and http-proxy-middleware
- `iView` UI components library
- `vue-lazyload` help us lazyload images
- `rem` + `flex` + `grid` responsive layout in mobile
- `yarn` package manager.
- `postman` test our interface

## Functions

敬请期待

## Directory
```
|
|—— build 
|—— config
|—— server
| |—— Node/ : The Back-End with `Node.js`
| |__ Python/ : The Back-End with `Python`
|
|——src : dev resources.
| |—— assets : images
| |—— components/
| |    |____ Common/ : reusable components
| |    |____ ... : other components of the own page.
| |
| |—— router/
| |    |____ index.js : the entry of router.
| |    |____ server.js : export ajax function.
| |    |____ serverConfig.js : export the server detail.
| |    |____ routes/ : every page's router, changing the state of `vuex` at its lifecycle function.
| |
| |—— store : vuex
| |—— App.vue : vue-draw-something
| |__ main.js : the entry of vue-draw-something
|
|__ static : static files

```

## Support

Thanks for you support,being glad for your `star`, `pr`, `follow` and `issue`.

When you see bugs.You can mail to me! me@xingbofeng.com !
