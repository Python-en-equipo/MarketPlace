import { createSlice } from "@reduxjs/toolkit";
export const categorySlice = createSlice({
  name:'category',
  initialState: {
    categories: [],
    loading: true
  },
  reducers:{
    setLoading: (state, action) =>{
      state.loading = !action.payload
    },
    setCategories: (state, action) =>{
      state.categories = action.payload
    }
  }
})

export const { setCategories, setLoading } = categorySlice.actions

export default categorySlice.reducer