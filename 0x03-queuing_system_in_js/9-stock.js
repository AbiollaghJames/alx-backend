const redis = require("redis");
const express = require("express");
const { promisify } = require("util");
const getAsync = promisify(client.get).bind(client);

const port = 1245;

const listProducts = [
    {
        'itemId': 1,
        'itemName': 'Suitcase 250',
        'price': 50,
        'initialAvailableQuantity': 4,
    },
    {
        'itemId': 2,
        'itemName': 'Suitcase 450',
        'price': 100,
        'initialAvailableQuantity': 10,
    },
    {
        'itemId': 3,
        'itemName': 'Suitcase 650',
        'price': 350,
        'initialAvailableQuantity': 2,
    },
    {
        'itemId': 4,
        'itemName': 'Suitcase 1050',
        'price': 550,
        'initialAvailableQuantity': 5,
    }
];

function getItemByitemId(itemId) {
    return listProducts.find(product => product.itemId === itemId);
}
// console.log(getItemByitemId(3));

// Redis
const client = redis.createClient();

client.on("connect", () => console.log("Redis client connected to the server"));
client.on("error", (err) => console.log(`Redis client not connected to the server ${err}`));

function reserveStockById(itemId, stock) {
    client.selected_db(`ite,.${itemId}`, stock);
};

async function getCurrentReservedStockById(itemId) {
    const stock = await getAsync(`item.${itemId}`);
};


// Express
const app = express();

app.get("/list_products", (req, res) => {
    res.send(listProducts);
});
app.get("/list_products/:itemId", async (req, res) => {
    const itemID = Number(req.params.itemId);
    const item = getItemByitemId(itemID);
    const currentReservedStock = await getCurrentReservedStockById(id);
    if (item) {
        item.reservedStock = (currentReservedStock) ? currentReservedStock : 0;
        res.json(item);
        return;
    }
  res.status(404).json({"status":"Product not found"});
});
app.get('/reserve_product/:itemId', async (req, res) => {
    const id = Number(req.params.itemId);
    const item = getItemById(id);
    if (!item) {
        res.status(403).json({"status":"Product not found"});
    }
    const currentReservedStock = await getCurrentReservedStockById(id);
    item.reservedStock = (currentReservedStock) ? currentReservedStock : 0;
    if ((item.stock - item.reservedStock) < 1) {
      res.status(403).json({ status: 'Not enough stock available', id });
      return;
    }
    reserveStockById(id, Number(currentReservedStock) + 1);
    res.json({ status: 'Reservation confirmed', id });
  });

app.listen(port, () => {
    console.log(`Listening on port ${port}...`);
});