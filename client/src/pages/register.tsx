import { useState } from "react"
import { useNavigate } from "react-router-dom"
import { api } from "../api/axios"
function Register()
{
const [nombreCompleto, setNombreCompleto] = useState("")
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [numero, setNumero] = useState<number>()

    const navigate = useNavigate()

    const btnRegister = async () => {
        try{
            if(!nombreCompleto || !email || !password || !numero){
                console.log("Nombre",nombreCompleto)
                console.log("Email: ", email)
                console.log("Password: ", password)
                console.log("Numero: ",numero)
                return;
            }
            const res = await api.post("/register",{nombre_completo: nombreCompleto,email,password,telefono:numero})
            console.log(res.data.nombre_completo)
        } catch(err){
            console.error(err)
        }
        
        
        // navigate("/home") // en caso de exito
    }
    const btnLogin = () => {
        navigate("/login")
    }
    return (
        <div className="flex items-center justify-center min-h-screen bg-lime-100">
            <form className="flex flex-col bg-cyan-200 rounded-2xl w-80 p-2 space-y-2">
                <h1 className="text-center">Registrase</h1>
                <label htmlFor="nombre">Nombre completo</label>
                <input className="bg-blue-100" type="text" id="nombre" onChange={(e)=> setNombreCompleto(e.target.value)} />
                <label htmlFor="email">Correo electronico</label>
                <input className="bg-blue-100" type="email" id="email" onChange={(e)=> setEmail(e.target.value)} />
                <label htmlFor="password">Contraseña</label>
                <input className="bg-blue-100" type="password" id="password" onChange={(e)=>setPassword(e.target.value)}/>
                <label htmlFor="number">Numero</label>
                <input className="bg-blue-100" type="tel" id="number" onChange={(e)=>setNumero(Number(e.target.value))}/>
                <button type="button" className="bg-blue-400 self-center w-1/3" onClick={btnRegister}>Registrase</button>
                <button type="button" className="bg-blue-400 self-center w-1/3" onClick={btnLogin}>Login</button>
            </form>
        </div>
    )
}

export default Register

