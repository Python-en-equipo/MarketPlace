import example from '../../assets/img/media/exampleproduct.jpeg'
const Item = ({product}) => {
  return (
    <figure className=' drop-shadow-xl bg-white rounded-xl overflow-hidden'>
      <h1 className='text-center text-lg'>{product}</h1>
      <img src={example} alt="example"/>
    </figure>
  )
}

export default Item