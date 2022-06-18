import { Route, Routes } from "react-router-dom";
import Layout from "./components/Layout";
import PageNotFound from "./components/PageNotFound";
import About from "./pages/About/About";
import Contact from "./pages/Contact/Contact";
import Home from "./pages/Home/Home";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Login from "./pages/Login/Login";
import Product from "./pages/Product/Product";
import Products from "./pages/Products/Products";
import Profile from "./pages/Profile/Profile";
import ProfileSeller from "./pages/ProfileSeller/ProfileSeller";

function App() {
  return (
    <>
    <Header/>
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/" element={<Layout />}>
        <Route index element={<Home />} />
        <Route path="contact" element={<Contact />} />
        <Route path="about" element={<About />} />
        <Route path="products" element={<Products />} />
        <Route path="product" element={<Product />} />
        {/*Desconozco pero logica elias: Si es usuario renderizar Profile, si no es, renderizar ProfileSeller */}
      </Route>
      <Route path="profile" element={<Profile />} />
      <Route path="profile-seller" element={<ProfileSeller />} />
      <Route path="*" element={<PageNotFound />} />
    </Routes>
    <Footer/>
    </>
  );
}

export default App;
