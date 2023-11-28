import { redis } from "redis";
const client = redis.createClient();

client.on("connetc", () => {
    console.log("Redis client connected to the server");
});
client.on("error", (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
});

const key = "HolbertonSchools";
const value = {
    'Portland': 50,
    'Seattle': 80,
    'New York': 20,
    'Bogota': 20,
    'Cali': 40,
    'Paris': 2
}

for (const [k, v] of Object.entries(value)) {
    client.hset(key, k, v, (err, reply) => 
    redis.print(`Reply: ${reply}`));
}

client.hgetall(key, (err, reply) => console.log(reply));