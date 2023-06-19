import { createClient, print } from 'redis';


const client = createClient(); // create a redis client

const KEY = 'HolbertonSchools';
const keys = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2];

keys.forEach((key, idx) => {
  client.hset(KEY, key, values[idx], print);
});

client.hgetall(KEY, (error, value) => {
  console.log(value);
});


