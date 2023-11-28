/**
 *  let’s use the client to store a hash value
 */

const redis = require('redis');

const client = redis.createClient();

const hashKey = 'HolbertonSchools';
const hashValues = {
  portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2
};

Object.entries(hashValues).forEach(([field, value]) => {
  client.hset(hashKey, field, value, (error, reply) => {
    if (error) {
      console.log(`Error setting value for ${field}:`, error);
    } else {
      console.log(`Value set for ${field}:`, reply);
    }
  });
});

client.hgetall(hashKey, (error, result) => {
  if (error) {
    console.error('Error retrieving hash values:', error);
  } else {
    console.log('Hash values in Redis:', result);
    Object.entries(result).forEach(([field, value]) => {
      console.log(`${field}: ${value}`);
    });
  }
  client.quit();
});
