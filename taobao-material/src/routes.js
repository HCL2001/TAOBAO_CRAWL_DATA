import Dashboard from "layouts/dashboard";
import Tables from "layouts/tables";
import Billing from "layouts/billing";
import RTL from "layouts/rtl";
import Notifications from "layouts/notifications";
import Profile from "layouts/profile";
import SignIn from "layouts/authentication/sign-in";
import SignUp from "layouts/authentication/sign-up";
import ListData from "layouts/listdata";
import DetailPage from "layouts/detail";

// @mui icons
import Icon from "@mui/material/Icon";

const routes = [
  {
    type: "collapse",
    name: "Dashboard",
    key: "dashboard",
    icon: <Icon fontSize="small">dashboard</Icon>,
    route: "/dashboard",
    component: <Dashboard />,
  },
  {
    type: "collapse",
    name: "Tables",
    key: "tables",
    icon: <Icon fontSize="small">table_view</Icon>,
    route: "/tables",
    component: <Tables />,
  },
  {
    type: "collapse",
    name: "List data",
    key: "list-data",
    icon: <Icon fontSize="small">assignment</Icon>,
    route: "/list",
    component: <ListData />,
  },
  {
    type: "collapse",
    name: "Profile",
    key: "profile",
    icon: <Icon fontSize="small">person</Icon>,
    route: "/profile",
    component: <Profile />,
  },
  {
    // ...các tuyến khác
  },
  {
    // Thêm tuyến cho trang chi tiết
    type: "collapse",
    name: "Detail Page", // Tên hiển thị trên menu
    key: "detail-page", // Khóa duy nhất cho tuyến
    route: "/detail/:id", // Định dạng URL cho trang chi tiết, :id sẽ được thay bằng ID thực tế
    component: <DetailPage />, // Sử dụng component DetailPage đã import
  },
  {
    // type: "collapse",
    // name: "Sign In",
    // key: "sign-in",
    // icon: <Icon fontSize="small">login</Icon>,
    route: "/",
    component: <SignIn />,
  },
  {
    type: "collapse",
    name: "Sign Up",
    key: "sign-up",
    icon: <Icon fontSize="small">assignment</Icon>,
    route: "/authentication/sign-up",
    component: <SignUp />,
  },
];

export default routes;
