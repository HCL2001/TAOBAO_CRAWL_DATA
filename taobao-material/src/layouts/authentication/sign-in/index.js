import React, { useEffect, useMemo, useState } from "react";
import axios from "axios";
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "@mui/material/TextField";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import Link from "@mui/material/Link";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import { useNavigate } from "react-router-dom";
// import { useSelector } from "react-redux";
// import { themeSettings } from "theme";
import { CircularProgress } from "@mui/material";
// import { API_BASE_URL } from "../api/api.jsx";
// react-router-dom components
// import { Link } from "react-router-dom";
import { API_BASE_URL } from "assets/api/api";
// @mui material components
import Card from "@mui/material/Card";
import Switch from "@mui/material/Switch";
import MuiLink from "@mui/material/Link";

// @mui icons
import FacebookIcon from "@mui/icons-material/Facebook";
import GitHubIcon from "@mui/icons-material/GitHub";
import GoogleIcon from "@mui/icons-material/Google";

// Material Dashboard 2 React components
import MDBox from "components/MDBox";
import MDTypography from "components/MDTypography";
import MDInput from "components/MDInput";
import MDButton from "components/MDButton";

// Authentication layout components
import BasicLayout from "layouts/authentication/components/BasicLayout";

// Images
import bgImage from "assets/images/bg-sign-in-basic.jpeg";

export default function Login() {
  // const [rememberMe, setRememberMe] = useState(false);

  // const handleSetRememberMe = () => setRememberMe(!rememberMe);

  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(false);
  const authToken = JSON.parse(JSON.stringify(localStorage.getItem("token")));
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  // const mode = useSelector((state) => state.global.mode);

  // const theme = useMemo(() => createTheme(themeSettings(mode)), [mode]);

  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    try {
      const response = await axios.post(API_BASE_URL + "/login", {
        username,
        password,
      });
      console.log(response.data);
      if (response.data.token) {
        localStorage.setItem("token", response.data.token);
        navigate("/dashboard");
      } else {
        setError(true);
      }
    } catch (error) {
      setError(true);
    }
    setIsLoading(false);
  };
  const checkToken = async () => {
    try {
      const response = await axios.post(API_BASE_URL + "/expired/", {
        token: authToken,
      });
      if (response.data) {
        navigate("/dashboard");
      }
      console.log(response.data);
    } catch (error) {
      console.error("Lỗi khi gửi yêu cầu:", error);
    }
  };

  useEffect(() => {
    checkToken();
  }, []);
  return (
    <BasicLayout image={bgImage}>
      <MDBox
        variant="gradient"
        bgColor="info"
        borderRadius="lg"
        coloredShadow="info"
        mx={2}
        mt={-3}
        p={2}
        mb={1}
        textAlign="center"
      >
        <Container component="main" maxWidth="mt">
          {" "}
          {/* Đổi maxWidth để tăng kích thước của form */}
          <CssBaseline />
          <Box
            sx={{
              width: 300,
              alignItems: "center",
              marginTop: 8,
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
              backgroundColor: "#F4F6F8", // Đổi màu nền sang màu sáng
              padding: "40px", // Tăng kích thước lề để tăng kích thước của form
              borderRadius: "10px", // Đổi bo góc nếu cần
              boxShadow: "0px 4px 10px rgba(0, 0, 0, 0.2)", // Thêm shadow nếu cần
            }}
          >
            <Avatar sx={{ m: 1, bgcolor: "secondary.main" }}>
              <LockOutlinedIcon />
            </Avatar>
            <Typography component="h1" variant="h5">
              Sign in
            </Typography>
            <Box component="form" onSubmit={(e) => handleLogin(e)} noValidate sx={{ mt: 1 }}>
              <TextField
                margin="normal"
                required
                fullWidth
                id="username"
                label="Username"
                name="username"
                autoComplete="username"
                autoFocus
                onChange={(e) => {
                  setUsername(e.target.value);
                }}
                error={error ? true : false}
                helperText={error ? "Wrong Username" : ""}
              />
              <TextField
                margin="normal"
                required
                fullWidth
                name="password"
                label="Password"
                type="password"
                id="password"
                autoComplete="current-password"
                onChange={(e) => {
                  setPassword(e.target.value);
                }}
                error={error ? true : false}
                helperText={error ? "Wrong Password" : ""}
              />
              <FormControlLabel
                control={<Checkbox value="remember" color="primary" />}
                label="Remember me"
              />
              <Button
                type="submit"
                fullWidth
                variant="contained"
                sx={{
                  mt: 3,
                  mb: 2,
                  backgroundColor: "#1976D2",
                  color: "#FFFFFF",
                }}
              >
                {isLoading ? <CircularProgress value={50} size={20} /> : "Sign in"}
              </Button>

              <Grid item xs={12}>
                <Link href="#" variant="body2">
                  Forgot password?
                </Link>
              </Grid>
              <Grid item xs={12}>
                <Link href="#" variant="body2">
                  {"Don't have an account?"}
                </Link>
              </Grid>
              <Grid item xs={12}>
                <Link href="#" variant="body2">
                  {"Sign Up"}
                </Link>
              </Grid>
            </Box>
          </Box>
          {/* <Copyright sx={{ mt: 8, mb: 4 }} /> */}
        </Container>
      </MDBox>
    </BasicLayout>
  );
}
