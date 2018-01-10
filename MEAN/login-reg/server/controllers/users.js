const mongoose = require('mongoose');
const User = mongoose.model('User');
const bcrypt = require('bcryptjs');

class UsersController{
    create(req, res){
        console.log(req.body)
        if(req.body.password != req.body.passwordConfirmation){
            return res.status(403).json("passwords don't match")
        }
        User.create(req.body, (err, user) =>{
            if(err){
                return res.status(403).json("failed to save user");
            }
            else{
                req.session.user_id = user.id;
                return res.status(200).json(user);
            }
        })
    }
    authenticate(req, res){
        User.findOne({email: req.body.email}, (err, user) =>{
            if(err){
                return res.status(403).json(err);
            }
            if(user && user.authenticate(req.body.password)){
                req.session.user_id = user.id;
                return res.status(200).json(user);
            }
            return res.status(403).json({
                errors: {
                    login: {
                        message: "invalid creditials"
                    }
                }
            })    
        })
    }
    session(req, res){
        if(!req.session.user_id){
            return res.json({ status: false})
        } 
        User.findById(req.session.user_id, (err, user) => {
            if (err){
                return res.json(err)
            }
            else{
                return res.json(user)
            }
        })
    }
    logout(req, res){
        delete req.session.user_id;
        return res.json({
            status: false
        })
    }
}

module.exports = new UsersController();