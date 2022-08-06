import { createSlice } from "@reduxjs/toolkit";

export const userSlice = createSlice({
  name:'user',
  initialState: {
    user: {
      email:'', 
      firstName: '',
      lastName:''
    },
    loading: false, 
  },
  reducers:{
    setUserData:(state, action) =>{
      state.user.email = action.payload.email
      state.user.firstName = action.payload.first_name
      state.user.lastName = action.payload.last_name
    }
  }
})

export const { setUserData } = userSlice.actions

export default userSlice.reducer