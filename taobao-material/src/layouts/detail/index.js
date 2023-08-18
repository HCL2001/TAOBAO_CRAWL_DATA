import { Typography, Divider, Paper, Container, Grid, Button } from "@mui/material";
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import React, { useEffect, useState } from "react";
import { API_BASE_URL } from "assets/api/api";
import { useParams } from "react-router-dom";

import axios from "axios";

const DetailPage = () => {
  const [productInfo, setProductInfo] = useState(null);
  const [data, setData] = useState([]);
  const authToken = JSON.parse(JSON.stringify(localStorage.getItem("token")));
  console.log(authToken);

  const fetchProductInfo = async () => {
    try {
      const token = localStorage.getItem("token");
      console.log("hieu" + token);
      if (!token) {
        console.error("Token not found in local storage");
        return;
      }

      const headers = new Headers({
        Authorization: `Bearer ${authToken}`,
        "Content-Type": "application/json",
      });

      const options = {
        method: "GET",
        headers: headers,
      };

      const response = await fetch(`${API_BASE_URL}/detail/{id}`, options);
      const data = await response.json();
      console.log("data", JSON.stringify(data));

      setProductInfo(data);
    } catch (error) {
      console.error("Error fetching product info:", error);
    }
  };

  useEffect(() => {
    fetchProductInfo();
  }, []);

  const firstSku = productInfo?._skus?.[0] || {};
  const originPrice = firstSku.origin_price || 0;
  const salePrice = firstSku.sale_price || 0;

  return (
    <DashboardLayout>
      <Container>
        <Paper elevation={3} sx={{ padding: 3, marginBottom: 3 }}>
          <Grid container spacing={3}>
            <Grid item xs={12} sm={6}>
              {productInfo && productInfo._main_imgs.length > 0 && (
                <div>
                  <img
                    src={productInfo._main_imgs[0]}
                    style={{ maxWidth: "100%", height: "auto", marginBottom: "10px" }}
                    alt={productInfo._title}
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
                      {productInfo && productInfo._title && (
                        <Typography variant="h6" color="textPrimary">
                          {productInfo._title}
                        </Typography>
                      )}
                      <Divider sx={{ marginY: 1 }} />
                    </Grid>
                  </Grid>
                </div>
                <div className="product-prices" style={{ display: "flex", alignItems: "baseline" }}>
                  <Typography variant="body2" color="textSecondary" style={{ marginRight: "5px" }}>
                    <strong>Origin Price:</strong>
                  </Typography>
                  <Typography variant="body2" color="textSecondary">
                    ${originPrice}
                  </Typography>
                </div>
                <div className="product-price" style={{ display: "flex", alignItems: "baseline" }}>
                  <Typography variant="body2" color="textSecondary" style={{ marginRight: "5px" }}>
                    <strong>Sale Price:</strong>
                  </Typography>
                  <Typography variant="body2" color="textSecondary">
                    ${salePrice}
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
