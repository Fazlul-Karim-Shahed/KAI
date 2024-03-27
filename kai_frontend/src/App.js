import { RouterProvider } from "react-router-dom";
import { router } from "./Routes/Route";
import Store from "./Redux/Store";
import { Provider } from "react-redux";



function App() {
  return (
    <Provider store={Store}>
      <RouterProvider router={router} />
    </Provider>
  );
}

export default App;
