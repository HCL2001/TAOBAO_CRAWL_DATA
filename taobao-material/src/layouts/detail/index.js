import React from "react";
import { Typography, Divider, Paper, Container, Grid, Button } from "@mui/material";
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";

const productDetail = {
  id: 718846337994,
  name: "Product Name",
  price: 100.0,
  promotion: "50% off",
  colors: ["Red", "Blue", "Green"],
  sizes: ["S", "M", "L"],
};

const DetailPage = () => {
  return (
    <DashboardLayout>
      <Container>
        <Paper elevation={3} sx={{ padding: 3, marginBottom: 3 }}>
          <Grid container spacing={3}>
            <Grid item xs={12} sm={6}>
              {/* Product Image */}
              <img
                src="https://vapa.vn/wp-content/uploads/2022/12/anh-3d-thien-nhien-001.jpg"
                style={{ maxWidth: "100%", height: "auto" }}
                alt={productDetail.name}
              />
            </Grid>
            <Grid item xs={12} sm={6}>
              {/* Product Information */}
              <Typography variant="h5">{productDetail.name}</Typography>
              <Typography variant="body2" color="textSecondary">
                Price: ${productDetail.price}
              </Typography>
              <Typography variant="body2" color="textSecondary">
                Promotion: {productDetail.promotion}
              </Typography>
              <Divider sx={{ marginY: 2 }} />
              <Typography variant="subtitle1">Colors:</Typography>
              <div>
                {productDetail.colors.map((color, index) => (
                  <Button
                    key={index}
                    variant="outlined"
                    color="primary"
                    sx={{
                      marginRight: 1,
                      backgroundColor: color.toLowerCase(), // Sử dụng màu sắc như background color
                      color: "white", // Màu chữ trắng để tương phản với nền
                    }}
                  >
                    {color}
                  </Button>
                ))}
              </div>
              <Typography variant="subtitle1">Sizes:</Typography>
              <div>
                {productDetail.sizes.map((size, index) => (
                  <Button key={index} variant="outlined" color="primary" sx={{ marginRight: 1 }}>
                    {size}
                  </Button>
                ))}
              </div>
              <Typography variant="subtitle1">Quantity:</Typography>
              <Button variant="outlined" color="primary">
                Add to Cart
              </Button>
            </Grid>
          </Grid>
        </Paper>
      </Container>
    </DashboardLayout>
  );
};

export default DetailPage;
