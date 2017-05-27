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
- `Mongo`

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
.
├── LICENSE
├── README.md
├── README_ZH.md
├── build
│   ├── build.js
│   ├── check-versions.js
│   ├── dev-client.js
│   ├── dev-server.js
│   ├── utils.js
│   ├── vue-loader.conf.js
│   ├── webpack.base.conf.js
│   ├── webpack.dev.conf.js
│   ├── webpack.prod.conf.js
│   └── webpack.test.conf.js
├── config
│   ├── dev.env.js
│   ├── index.js
│   ├── prod.env.js
│   └── test.env.js
├── index.html
├── package.json
├── src
│   ├── client
│   │   ├── App.vue
│   │   ├── assets
│   │   │   ├── draw-something.jpg
│   │   │   └── logo.jpeg
│   │   ├── components
│   │   │   ├── Chatting.vue
│   │   │   ├── Layout.vue
│   │   │   ├── LeftDrawer.vue
│   │   │   ├── TopHeader.vue
│   │   │   ├── p_about
│   │   │   │   └── ExplainCard.vue
│   │   │   ├── p_guess
│   │   │   │   ├── Board.vue
│   │   │   │   └── GuessAnswer.vue
│   │   │   ├── p_home
│   │   │   ├── p_login
│   │   │   │   └── LoginBox.vue
│   │   │   ├── p_paint
│   │   │   │   └── PaintContent.vue
│   │   │   └── p_signup
│   │   │       └── SignupBox.vue
│   │   ├── currency.js
│   │   ├── main.js
│   │   ├── pages
│   │   │   ├── About.vue
│   │   │   ├── Guess.vue
│   │   │   ├── Home.vue
│   │   │   ├── Login.vue
│   │   │   ├── Paint.vue
│   │   │   └── Signup.vue
│   │   ├── plugins
│   │   │   ├── devtool.js
│   │   │   └── logger.js
│   │   ├── router
│   │   │   └── index.js
│   │   ├── serverConfig.json
│   │   ├── store
│   │   │   ├── actions.js
│   │   │   ├── getters.js
│   │   │   ├── index.js
│   │   │   ├── mutation-types.js
│   │   │   ├── mutations.js
│   │   │   └── state.js
│   │   └── util.js
│   └── server
│       ├── node
│       │   └── index.js
│       └── python
│           ├── index.py
│           └── lib
│               ├── login
│               │   ├── __init__.py
│               │   └── login.py
│               ├── logout
│               │   ├── __init__.py
│               │   └── logout.py
│               ├── signup
│               │   ├── __init__.py
│               │   └── signup.py
│               └── user
│                   ├── __init__.py
│                   └── user.py
├── static
└── yarn.lock

```

## Support

Thanks for you support,being glad for your `star`, `pr`, `follow` and `issue`.

When you see bugs.You can mail to me! me@xingbofeng.com !
