const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');

let UserSchema = new mongoose.Schema({
    name:{type: String},
    email:{type: String},
    password:{type: String},
    passwordConfirmation: {type: String},
}, {timestamps:true});

UserSchema.pre('save', function(next){
    this.password = bcrypt.hashSync(this.password, bcrypt.genSaltSync(8));
    next();
});

UserSchema.methods.authenticate = function(password){
    return bcrypt.compareSync(password, this.password);
}

mongoose.model('User', UserSchema);