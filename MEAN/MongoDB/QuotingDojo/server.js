var express = require('express');
var session = require('express-session');
var app = express();
app.use(session({secret: 'codingdojorocks'}));
var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));
var path = require('path');
app.use(express.static(path.join(__dirname, './static')));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/basic_mongoose');
mongoose.Promise = global.Promise;

var QuoteSchema = new mongoose.Schema({
    name:{
        type: String,
        required: true,
        min: [2, 'Name too short'],
    },
    quote:{
        type: String,
        required: true,
        min: [10, 'Quote must be at least 10 characters long']
    }
});

mongoose.model('Quote', QuoteSchema);
var Quote = mongoose.model('Quote')

app.get('/', function(req, res) {
    res.render('index');
})
app.post('/post_quote', function(req, res) {
    console.log("New")
    var quote = new Quote({name: req.body.name, quote:req.body.quote});
    quote.save(function(err){
        if(err){
            console.log('something went wrong');
            res.redirect('/')
        }
        else{
            console.log('successfully added quote');
            res.redirect('/quotes')
        }
    })
})

app.get('/quotes', function(req, res){
    Quote.find({}, function(err, quotes){
        if(quotes.length<1){
            console.log("no quotes found")
            res.redirect
        }
        else{
            console.log(quotes)
            res.render('quotes', {"quotes":quotes});
        }
    })
})

app.listen(8000, function() {
})
