/**
 * In a file named 5-subscriber.js, create a redis client:
 */
import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log('Redis client not connected to the server:', error);
});

channel = 'holberton school channel';
client.subscribe(channel);

client.on('message', (_err, messsage) => {
  console.log(messsage);
  if (messsage === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});
