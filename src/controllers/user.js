const db = require('../dbClient')

module.exports = {
  create: (user, callback) => {
    // Check parameters
    if(!user.username)
      return callback(new Error("Wrong user parameters"), null)
    // Create User schema
    const userObj = {
      firstname: user.firstname,
      lastname: user.lastname,
    }
    // Save to DB
    // TODO check if user already exists
    db.hmset(user.username, userObj, (err, res) => {
      if (err) return callback(err, null)
      callback(null, res) // Return callback
    })
  },
get: (username, callback) => {
  if (!username) {
    return callback(new Error('Username is required'), null)
  }

  db.hgetall(username, (err, data) => {
    if (err) {
      return callback(err, null)
    }

    if (!data) {
      return callback(new Error('User not found'), null)
    }

    // Redis returns all hash fields as strings, reconstruct proper user object
    const user = {
      username: username,
      firstname: data.firstname,
      lastname: data.lastname
    }

    callback(null, user)
  })
},

}

