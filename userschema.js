const { Decimal128 } = require("bson");
const mongoose = require("mongoose");
const userschema = new mongoose.Schema({
    latn: {
        type:Decimal128,
        required:true
    },
    longw: {
        type:Decimal128,
        required:true
    },
    traffic: {
        type:Decimal128,
        required:true
    },
    signal: {
        type:String,
        required:true
    }
})

const User = mongoose.model('map1', userschema);
module.exports = User;