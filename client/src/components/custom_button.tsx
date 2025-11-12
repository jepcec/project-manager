interface ICustomButton{
    label: string;
    onClick: ()=>void;
}
const CustomButton = ({label,onClick}:ICustomButton) =>(
    <button onClick={onClick} className="bg-fuchsia-300">
        {label}
    </button>
)


export default CustomButton
