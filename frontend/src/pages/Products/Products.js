import { useEffect } from 'react'
import {useDispatch, useSelector} from 'react-redux'
import Spinner from '../../components/Spinner'
import { setLoading } from '../../store/slices/category'
import { getCategories } from '../../store/slices/category/services'
import Category from './Category'

function Products() {
  const dispatch = useDispatch()
  const {categories, loading} = useSelector(state => state.categoryReducer)

  useEffect(() =>{
    dispatch(getCategories())
    //el timeout es solo para que se vea el loading no es importante xd
    setTimeout(() => dispatch(setLoading(loading)), 1000)}
  ,[dispatch])

  return (
    <>
    {loading
    ?<Spinner/>
    :(<section className='mt-44'>
      {categories.map(category => <Category key={category.id} category={category}/>)}
    </section>)
    } 
    </>
   
  )
}

export default Products;
