const mysql = require('mysql2/promise')
require('dotenv').config();
console.log("Hola",process.env.DB_PASSWORD);
const pool = mysql.createPool({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
  connectionLimit: 5,
});

async function testConnection() {
  let connection;
  try {
    connection = await pool.getConnection();
    console.log('Conectado a MariaDB (mysql2)');
    connection.release(); 
    return true; 
  } catch (err) {
    console.error('Error conexión a MariaDB:', err);
    return false; 
  }
}
module.exports = { pool, testConnection };