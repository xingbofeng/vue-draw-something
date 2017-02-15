var server = require('http').createServer();
var io = require('socket.io')(server);
io.on('connection', function (client) {
	client.on('paint', function (message) {
		// 用io.sockets.emit 才能向所有客户端广播！
		// 画图中
		client.broadcast.emit('painting', message);
	});
	client.on('begin', function (message) {
		// 开始画图
		client.broadcast.emit('began', message);
	});
	client.on('clear', function () {
		// 清除操作
		client.broadcast.emit('clear');
	});
});
server.listen(2017, function () {
	console.log('server run http://localhost:2017.');
});