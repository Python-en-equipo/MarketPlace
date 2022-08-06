import { setUserData } from './index'

export const createUser = (data) => (dispatch) =>{
  const body = new FormData()
    body.append("email",data.email)
    body.append("first_name", data.firstName)
    body.append("last_name", data.lastName)
    body.append("password", data.password)
    body.append("password2", data.confirmPassword)
  fetch('http://django-ecommerce-v1.herokuapp.com/api/v1/users/',{
    method:'POST',
    body
  })
  .then(res => res.json())
  .then(res =>{
      dispatch(setUserData(res))
      saveToken({email:data.email, password:data.password})
    })
}

export const loginUser = async (data) =>{
    if(await saveToken(data)){
      return true
    }
    return false
} 

export const saveToken = (data) =>{
  const body = new FormData()
  body.append("email", data.email)
  body.append("password", data.password)
  fetch('http://django-ecommerce-v1.herokuapp.com/api/v1/users/token/',{
    method:'POST',
    body
  })
  .then(res => res.json())
  .then(res =>{
    window.localStorage.setItem('token', res.access)
    window.localStorage.setItem('refresh', res.refresh)
    })
}
