import { configureStore } from '@reduxjs/toolkit'
import categoryReducer from './slices/category'
import productReducer from './slices/product'
import userReducer from './slices/user'
export default configureStore({
  reducer:{
    categoryReducer,
    productReducer,
    userReducer
  }
})