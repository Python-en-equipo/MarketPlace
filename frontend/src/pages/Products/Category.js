import React from 'react'
import Item from './Item'

const Categorie = ({category}) => {
  return (
      <section className='w-screen h-fit bg-gray-200 my-6 px-6 py-12'>
        <h1 className='text-xl font-bold mb-3'>{category.title}</h1>
        <div className='flex gap-6'>
          {category.products.map((product, i) =>
            <Item key={i} product={product} />
          )} 
        </div>
      </section>
  )
}

export default Categorie
