import Card from "@mui/material/Card";

// Material Dashboard 2 React components
import MDBox from "components/MDBox";
import MDTypography from "components/MDTypography";

// Material Dashboard 2 React example components
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import DashboardNavbar from "examples/Navbars/DashboardNavbar";
import Footer from "examples/Footer";
import DataTable from "examples/Tables/DataTable";

// Data
import authorsTableData from "layouts/tables/data/authorsTableData";
import projectsTableData from "layouts/tables/data/projectsTableData";
import axios from "axios";
import React, { useState } from "react";
import {
  Box,
  Button,
  Grid,
  TextField,
  useTheme,
  Modal,
  Typography,
  CircularProgress,
  Link,
} from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import Header from "examples/Header/Header";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { API_BASE_URL } from "assets/api/api";
import IconButton from "@mui/material/IconButton";
import FilterAltIcon from "@mui/icons-material/FilterAlt";
import ChevronRightIcon from "@mui/icons-material/ChevronRight";
function Search() {
  const authToken = JSON.parse(JSON.stringify(localStorage.getItem("token")));
  const [selectedRowIds, setSelectedRowIds] = useState([]);
  const [isButtonDisabled, setIsButtonDisabled] = useState(true);
  const theme = useTheme();
  const [form, setForm] = useState({});
  const [data, setData] = useState([]);
  const [selectedRows, setSelectedRows] = useState([]);
  const [loading, setLoading] = useState(false);
  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };
  const handleKeyDown = (event) => {
    if (event.key === "Enter") {
      handleSubmit();
    }
  };
  const handleSubmit = async (e) => {
    setLoading(true);
    if (form.search) {
      try {
        const response = await axios.get(API_BASE_URL + "/search/" + form.search, {
          headers: {
            Authorization: `Bearer ${authToken}`,
          },
        });
        setData(response.data);
        setSelectedRowIds([]);
        console.log(response.data);
        console.log("Yêu cầu đã được gửi thành công!");
      } catch (error) {
        if (error.message === "Request failed with status code 403") {
          window.location.reload();
        } else {
          toast.error(error.code, {
            position: toast.POSITION.TOP_CENTER,
            autoClose: 3000,
            hideProgressBar: true,
          });
        }
      }
    } else {
      toast.error("Bạn vui lòng nhập từ khóa vào ô search!", {
        position: toast.POSITION.TOP_CENTER,
        autoClose: 3000,
        hideProgressBar: true,
      });
    }
    setLoading(false);
    setIsButtonDisabled(true);
  };

  const [open, setOpen] = useState(false);

  const handleClose = () => {
    setOpen(false);
  };

  const handleConfirm = async () => {
    setOpen(false);
    try {
      const response = await axios.post(
        API_BASE_URL + "/link",
        {
          s_links: selectedRows,
          id_brand: 1,
        },
        {
          headers: {
            Authorization: `Bearer ${authToken}`,
          },
        }
      );
      console.log(response.data);
      if (response.data.size != 0) {
        toast.success("Bạn đã lưu " + response.data.size + " link thành công!", {
          position: toast.POSITION.TOP_CENTER,
          autoClose: 3000,
          hideProgressBar: true,
        });
      } else {
        toast.error("Link đã tồn tại!", {
          position: toast.POSITION.TOP_CENTER,
          autoClose: 3000,
          hideProgressBar: true,
        });
      }
    } catch (error) {
      if (error.message === "Request failed with status code 403") {
        window.location.reload();
      } else {
        toast.error(error.code, {
          position: toast.POSITION.TOP_CENTER,
          autoClose: 3000,
          hideProgressBar: true,
        });
      }
    }
  };
  const handleModal = async () => {
    setOpen(true);
  };

  const handleCancel = async () => {
    setOpen(false);
  };
  const columns = [
    {
      field: "id",
      headerName: "#",
      width: 50,
    },
    {
      field: "name",
      headerName: "Name",
      width: 400,
    },
    {
      field: "price",
      headerName: "Price",
      width: 100,
    },
    {
      field: "shopName",
      headerName: "Shop Name",
      width: 100,
    },
    {
      field: "link",
      headerName: "Link",
      width: 650,
      renderCell: (params) => {
        const linkUrl = params.value;
        return (
          <Link
            href={linkUrl}
            target="_blank"
            rel="noopener"
            sx={{
              color: "white",
              textDecoration: "none",
              overflow: "hidden",
              textOverflow: "ellipsis",
            }}
          >
            {linkUrl}
          </Link>
        );
      },
    },
  ];

  return (
    <DashboardLayout>
      <DashboardNavbar />
      <MDBox pt={6} pb={3}>
        <ToastContainer />
        <Header title="TAOBAO" subtitle="Search of Product" />
        <Box
          mt="40px"
          height="75vh"
          sx={{
            "& .MuiDataGrid-root": {
              border: "none",
            },
            "& .MuiDataGrid-cell": {
              borderBottom: "none",
            },
            "& .MuiDataGrid-columnHeaders": {
              backgroundColor: theme.palette.background.alt,
              color: theme.palette.secondary[100],
              borderBottom: "none",
            },
            "& .MuiDataGrid-virtualScroller": {
              backgroundColor: theme.palette.primary.light,
            },
            "& .MuiDataGrid-footerContainer": {
              backgroundColor: theme.palette.background.alt,
              color: theme.palette.secondary[100],
              borderTop: "none",
            },
            "& .MuiDataGrid-toolbarContainer .MuiButton-text": {
              color: `${theme.palette.secondary[200]} !important`,
            },
            "& .image": {
              borderRadius: "50%",
            },
            "& .MuiDataGrid-checkboxInput.Mui-checked": {
              color: "white",
            },
            "& .MuiDataGrid-root--densityStandard": {
              maxWidth: "1189.2px",
              maxHeight: "559.2px",
            },
            "& .MuiGrid-item": {
              maxWidth: "1189.2px",
            },
          }}
        >
          <Grid item xs={10} sm={8} md={6} lg={4}>
            <Box sx={{ display: "flex", mb: 3 }}>
              <TextField
                fullWidth
                label="Search"
                name="search"
                onChange={handleChange}
                variant="outlined"
                size="small"
                style={{ width: 200, minWidth: 200, maxWidth: 800 }}
                onKeyDown={handleKeyDown}
              />
              <IconButton onClick={handleSubmit}>
                {loading ? <CircularProgress size={24} /> : <FilterAltIcon />}
              </IconButton>
              <Button
                variant="contained"
                color="primary"
                style={{ marginLeft: "auto" }}
                onClick={handleModal}
                disabled={isButtonDisabled}
                endIcon={<ChevronRightIcon />}
              >
                Submit
              </Button>
            </Box>
          </Grid>
          <DataGrid
            getRowId={(row) => row.id}
            columns={columns}
            rows={data}
            checkboxSelection
            disableRowSelectionOnClick
            initialState={{
              ...data.initialState,
              pagination: { paginationModel: { pageSize: 10 } },
            }}
            pageSizeOptions={[10, 20, 30]}
            onRowSelectionModelChange={(ids) => {
              setSelectedRowIds(ids);
              const selectedIDs = new Set(ids);
              const selectedRows = data.filter((row) => selectedIDs.has(row.id));
              const selectedLinks = selectedRows.map((row) => ({
                name: row.link,
                link: row.link,
              }));
              setSelectedRows(selectedLinks);
              setIsButtonDisabled(selectedLinks.length === 0);
            }}
            rowSelectionModel={selectedRowIds}
          />
        </Box>
        <Modal open={open} onClose={handleClose}>
          <Box
            sx={{
              position: "absolute",
              top: "50%",
              left: "50%",
              transform: "translate(-50%, -50%)",
              width: 400,
              bgcolor: theme.palette.primary[700],
              borderRadius: 8,
              boxShadow: "0 2px 4px rgba(0, 0, 0, 0.2)",
              p: 4,
              textAlign: "center",
            }}
          >
            <Typography variant="h6" component="h2" sx={{ mb: 2 }}>
              Xác nhận Lưu vào Danh sách
            </Typography>
            <Typography variant="body1" component="p" sx={{ mb: 4 }}>
              Bạn có chắc chắn muốn lưu những sản phẩm đã chọn vào danh sách không?
            </Typography>
            <Box sx={{ display: "flex", justifyContent: "center" }}>
              <Button variant="contained" color="error" onClick={handleCancel} sx={{ mr: 2 }}>
                Cancel
              </Button>
              <Button variant="contained" color="primary" onClick={handleConfirm}>
                Confirm
              </Button>
            </Box>
          </Box>
        </Modal>
      </MDBox>
      <Footer />
    </DashboardLayout>
  );
}

export default Search;
