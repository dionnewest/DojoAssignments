//Cars and Cats
var http = require('http');

var fs = require('fs');

var server = http.createServer(function (request, response){

    console.log('client request URL: ', request.url);

    if(request.url === '/') {
        fs.readFile('index.html', 'utf8', function (errors, contents){
            response.writeHead(200, {'Content-Type': 'text/html'});
            response.write(contents); 
            response.end();
        });
    }
    else if(request.url === '/cars') {
        fs.readFile('cars.html', 'utf8', function (errors, contents){
            response.writeHead(200, {'Content-Type': 'text/html'});
            response.write(contents); 
            response.end();
        });
    }
    else if(request.url === '/cats') {
        fs.readFile('cats.html', 'utf8', function (errors, contents){
            response.writeHead(200, {'Content-Type': 'text/html'});
            response.write(contents); 
            response.end();
        });
    }
    else if(request.url === '/cars/new') {
        fs.readFile('new_car.html', 'utf8', function (errors, contents){
            response.writeHead(200, {'Content-Type': 'text/html'});
            response.write(contents); 
            response.end();
        });
    }
    else if(request.url === '/images/car1.jpg') {
        fs.readFile('images/car1.jpg', function (errors, contents){
            response.writeHead(200, {'Content-Type': 'image/jpg'});
            response.write(contents); 
            response.end();
        });
    }
    else if(request.url === '/images/car2.jpg') {
        fs.readFile('images/car2.jpg', function (errors, contents){
            response.writeHead(200, {'Content-Type': 'image/jpg'});
            response.write(contents); 
            response.end();
        });
    }
    else if(request.url === '/images/car3.jpg') {
        fs.readFile('images/car3.jpg', function (errors, contents){
            response.writeHead(200, {'Content-Type': 'image/jpg'});
            response.write(contents); 
            response.end();
        });
    }
    else if(request.url === '/images/car4.jpg') {
        fs.readFile('images/car4.jpg', function (errors, contents){
            response.writeHead(200, {'Content-Type': 'image/jpg'});
            response.write(contents); 
            response.end();
        });
    }
    else if(request.url === '/images/cat1.jpeg') {
        fs.readFile('images/cat1.jpeg', function (errors, contents){
            response.writeHead(200, {'Content-Type': 'image/jpeg'});
            response.write(contents); 
            response.end();
        });
    }
    else if(request.url === '/images/cat2.jpg') {
        fs.readFile('images/cat2.jpg', function (errors, contents){
            response.writeHead(200, {'Content-Type': 'image/jpg'});
            response.write(contents); 
            response.end();
        });
    }
    else if(request.url === '/images/cat3.jpeg') {
        fs.readFile('images/cat3.jpeg', function (errors, contents){
            response.writeHead(200, {'Content-Type': 'image/jpeg'});
            response.write(contents); 
            response.end();
        });
    }
    else if(request.url === '/images/cat4.jpg') {
        fs.readFile('images/cat4.jpg', function (errors, contents){
            response.writeHead(200, {'Content-Type': 'image/jpg'});
            response.write(contents); 
            response.end();
        });
    }
    else {
        response.end('File not found!!!');
    }
});
server.listen(7077);
console.log("Running in localhost at port 7077");
