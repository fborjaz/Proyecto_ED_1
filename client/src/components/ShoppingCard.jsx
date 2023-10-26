export function ShoppingCard({ shopping }) {
  return (
    <div key={shopping.id}>
    <h1>{shopping.name}</h1>
    <p>{shopping.description}</p>
  </div>
  )
}

