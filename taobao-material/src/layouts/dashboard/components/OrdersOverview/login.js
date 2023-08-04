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
import { useSelector } from "react-redux";
import { themeSettings } from "theme";
import { CircularProgress } from "@mui/material";
import { API_BASE_URL } from "../api/api.jsx";

function Copyright(props) {
  return (
    <Typography variant="body2" color="text.secondary" align="center" {...props}>
      {"Copyright © "}
      <Link color="inherit" href="https://mui.com/">
        Your Website
      </Link>{" "}
      {new Date().getFullYear()}
      {"."}
    </Typography>
  );
}

export default function Login() {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(false);
  const authToken = JSON.parse(JSON.stringify(localStorage.getItem("token")));
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const mode = useSelector((state) => state.global.mode);

  const theme = useMemo(() => createTheme(themeSettings(mode)), [mode]);

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
        navigate("/hasaki/search");
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
        navigate("/hasaki/search");
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
    <ThemeProvider theme={theme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
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
            <Button type="submit" fullWidth variant="contained" sx={{ mt: 3, mb: 2 }}>
              {isLoading ? <CircularProgress value={50} size={20} /> : "Sign in"}
            </Button>
            <Grid container>
              <Grid item xs>
                <Link href="#" variant="body2">
                  Forgot password?
                </Link>
              </Grid>
              <Grid item>
                <Link href="#" variant="body2">
                  {"Don't have an account? Sign Up"}
                </Link>
              </Grid>
            </Grid>
          </Box>
        </Box>
        <Copyright sx={{ mt: 8, mb: 4 }} />
      </Container>
    </ThemeProvider>
  );
}
