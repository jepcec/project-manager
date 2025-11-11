import { useState } from "react"
function Login()
{
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")

    const btnLogin = () => {
        console.log("Email: ", email)
        console.log("Password: ", password)
    }
    return (
        <div className="flex items-center justify-center min-h-screen bg-lime-100">
            <form className="flex flex-col bg-cyan-200 rounded-2xl w-80 p-2">
                <h1 className="text-center">Iniciar sesion</h1>
                <label htmlFor="email">Correo electronico</label>
                <input type="email" onChange={(e)=> setEmail(e.target.value)} />
                <label htmlFor="password">Password</label>
                <input type="password" onChange={(e)=>setPassword(e.target.value)}/>
                <button onClick={btnLogin}>Entrar</button>
                <button>Registrarse</button>
            </form>
        </div>
    )
}

export default Login
