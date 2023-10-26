import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import Home from './components/Home'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path = "/" element = {<Navigate to = "/shopping" />} />
        <Route path = "/shopping" element = {<Home />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App