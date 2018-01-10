var mongoose = require('mongoose');

var User = mongoose.model('User');

module.exports={
    show: function(req, res){
        res.render('index')
    },
    register: function(req, res){
        var user = new User ({first_name: req.body.first_name, last_name: req.body.last_name, email: req.body.email, password: req.body.password, dob: req.body.dob});
        user.save(function(err){
            if(err){
                console.log(err)
                return res.status(400).json(err.errors)
            }
            console.log(user)
            res.redirect('/')
        })
    }
}