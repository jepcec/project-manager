const {testConnection, pool} =require('./conf/database'); 

(async () => {
  const ok = await testConnection();
  if (!ok) 
    {
        console.log("No funcionando")
    }
      // si falla la conexión, detenemos la app
})();