
// var path = require('path');
// var bodyParser = require('body-parser');
// var server =require('http').createServer(app);
// var express = require('express');
// var app = express();
// var io=require('socket.io').listen(server);
// server.listen(3000);
// app.get('/',function(req,res){
//   res.sendFile(__dirname + '/index.html');
// });

// io.on('connection', function (socket) {
//   socket.emit('news', { hello: 'world' });
//   socket.on('my other event', function (data) {
//     console.log(data);
//   });
// });
var app = require('express')();
var http = require('http').createServer(app);
var io = require('socket.io').listen(http);

//Server accepting connect on this port
http.listen(3000);
// app.get('/',function(req,res){
//      res.sendFile(__dirname + '/index.html');
//    });

//Establishing connection to client and disconnecting
io.sockets.on('connection', function(socket){
    console.log('Connected to a new client');

    socket.on('error', function(err) {
        //here i change options
        console.log('Error!', err);
    });

    socket.on('room', function(room) {
        socket.join(room);
        console.log('join room: '+ room);
    });
    socket.on('disconnect', function(){
        // socket.disconnect();
        console.log('Disconnected from a client');
    });

    var room= 'room1';
    //Data exchange between client and server
    //Server receives new data from a client and broadcast it to others
    socket.on('client_character',function(msg){
        //receive data
        console.log('Data from client: '+msg.buffer);
        socket.in(room).broadcast.emit('server_character',msg.buffer);
        //socket.broadcast.to(room).emit('server_character', msg.buffer);
        //socket.to(room).emit('server_character',msg.buffer);

    });
  });

