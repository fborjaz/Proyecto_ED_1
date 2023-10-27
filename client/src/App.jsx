import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import Main from './components/Main'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path = "/" element = {<Navigate to = "/shooping" />} />
        <Route path = "/shopping" element = {<Main />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App