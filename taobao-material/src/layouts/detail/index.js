import { Typography, Divider, Paper, Container, Grid, Button } from "@mui/material";
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import React, { useEffect, useState } from "react";
import { API_BASE_URL } from "assets/api/api";
import { useParams } from "react-router-dom";
import axios from "axios";

// Import statements...

const DetailPage = () => {
  const { id } = useParams();
  console.log(id);
  const [productInfo, setProductInfo] = useState({
    price: "0.00",
    image: "",
    name: "Product Name",
  });

  const authToken = localStorage.getItem("token");

  const fetchProductInfo = async () => {
    try {
      if (!authToken) {
        console.error("Token not found in local storage");
        return;
      }

      const headers = {
        Authorization: `Bearer ${authToken}`,
        "Content-Type": "application/json",
      };

      const response = await fetch(`${API_BASE_URL}/detail/${id}`, { headers });
      const data = await response.json();

      setProductInfo(data);
    } catch (error) {
      console.error("Error fetching product info:", error);
    }
  };

  useEffect(() => {
    fetchProductInfo();
  }, []);

  return (
    <DashboardLayout>
      <Container>
        <Paper elevation={3} sx={{ padding: 3, marginBottom: 3 }}>
          <Grid container spacing={3}>
            <Grid item xs={12} sm={6}>
              {productInfo.image && (
                <div>
                  <img
                    src={productInfo.image}
                    style={{ maxWidth: "100%", height: "auto", marginBottom: "10px" }}
                    alt={productInfo.name}
                  />
                </div>
              )}
            </Grid>
            <Grid item xs={12} sm={6}>
              {/* Product Information */}
              <div style={{ display: "flex", flexDirection: "column" }}>
                <div className="product-info">
                  <Grid container spacing={1}>
                    <Grid item xs={12}>
                      <Typography variant="h6" color="textPrimary">
                        {productInfo.name}
                      </Typography>
                      <Divider sx={{ marginY: 1 }} />
                    </Grid>
                  </Grid>
                </div>
                <div className="product-prices" style={{ display: "flex", alignItems: "baseline" }}>
                  <Typography variant="body1" color="textSecondary" style={{ marginRight: "5px" }}>
                    <strong>Price:</strong>
                  </Typography>
                  <Typography variant="body1" color="textSecondary">
                    ¥{productInfo.price}
                  </Typography>
                </div>
              </div>
            </Grid>
          </Grid>
        </Paper>
      </Container>
    </DashboardLayout>
  );
};

export default DetailPage;
