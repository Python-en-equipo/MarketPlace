import { setCategories } from './index'

const baseUrl = "http://django-ecommerce-v1.herokuapp.com/api/v1"
export const getCategories = () =>  (dispatch) => {
  try {
    fetch(`${baseUrl}/categories/`)
    .then(res => res.json())
    .then(res =>{
      dispatch(setCategories(res))
    })
    
  } catch (error) {
    console.error(error)
  }
}