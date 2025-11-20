import { useState } from "react"
import { useNavigate } from "react-router-dom"
function Login()
{
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")

    const navigate = useNavigate()

    const btnLogin = () => {
        console.log("Email: ", email)
        console.log("Password: ", password)
        navigate("/home") // en caso de exito
    }
    const btnRegister = () => {
        navigate("/register")
    }
    return (
        <div className="flex items-center justify-center min-h-screen bg-lime-100">
            <form className="flex flex-col bg-cyan-200 rounded-2xl w-80 p-2 space-y-2">
                <h1 className="text-center">Registrarse</h1>
                <label htmlFor="email">Correo electronico</label>
                <input className="bg-blue-100" type="email" id="email" onChange={(e)=> setEmail(e.target.value)} />
                <label htmlFor="password">Password</label>
                <input className="bg-blue-100" type="password" id="password" onChange={(e)=>setPassword(e.target.value)}/>
                <button className="bg-blue-400 self-center w-1/3" onClick={btnLogin}>Entrar</button>
                <button className="bg-blue-400 self-center w-1/3" onClick={btnRegister}>Registrase</button>
            </form>
        </div>
    ) 
}

export default Login
