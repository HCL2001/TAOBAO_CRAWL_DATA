import Card from "@mui/material/Card";

// Material Dashboard 2 React components
import MDBox from "components/MDBox";
import MDTypography from "components/MDTypography";

// Material Dashboard 2 React example components
import DashboardLayout from "examples/LayoutContainers/DashboardLayout";
import DashboardNavbar from "examples/Navbars/DashboardNavbar";
import Footer from "examples/Footer";
import DataTable from "examples/Tables/DataTable";
import { Link as RouterLink } from "react-router-dom";

// Data
import authorsTableData from "layouts/tables/data/authorsTableData";
import projectsTableData from "layouts/tables/data/projectsTableData";
import axios from "axios";
import React, { useEffect, useState } from "react";
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
  Pagination,
} from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import Header from "examples/Header/Header";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { API_BASE_URL } from "assets/api/api";
import IconButton from "@mui/material/IconButton";
import FilterAltIcon from "@mui/icons-material/FilterAlt";
import ChevronRightIcon from "@mui/icons-material/ChevronRight";

function ListData() {
  const theme = useTheme();
  const [data, setData] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [isButtonDisabled, setIsButtonDisabled] = useState(true);
  const [selectedRowIds, setSelectedRowIds] = useState([]);
  const [selectedRows, setSelectedRows] = useState([]);
  const [loading, setLoading] = useState(false);
  const [open, setOpen] = useState(false);
  const [currentPage, setCurrentPage] = useState(1);

  const [page, setPage] = useState(1); // Current page
  const pageSize = 10; // Number of items per page

  const startIndex = (page - 1) * pageSize;
  const endIndex = startIndex + pageSize;

  // ... Your existing functions

  async function fetchListData(pageNumber, itemsPerPage) {
    const token = localStorage.getItem("token");
    const headers = new Headers({
      Authorization: `Bearer ${token}`,
      "Content-Type": "application/json",
    });

    const options = {
      method: "GET",
      headers: headers,
    };

    try {
      const response = await fetch(
        `${API_BASE_URL}/list?page_number=${pageNumber}&items_per_page=${itemsPerPage}`,
        options
      );
      if (!response.ok) {
        console.log("Error");
      }
      const data = await response.json();
      return data;
    } catch (error) {
      console.error("Error");
      return [];
    }
  }

  useEffect(() => {
    const fetchDataOnMount = async () => {
      setIsLoading(true);
      try {
        const newData = await fetchListData(currentPage, 10);
        if (newData !== null && newData !== undefined) {
          setData(newData);
          setIsButtonDisabled(newData.length === 0);
        } else {
          setIsButtonDisabled(true);
        }
      } catch (error) {
        console.error("Error:", error);
      }
      setIsLoading(false);
    };

    fetchDataOnMount();
  }, [currentPage]);

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
      renderCell: (params) => {
        const { id, name } = params.row;
        return (
          <RouterLink
            to={`/detail/${id}`}
            style={{
              color: "white",
              textDecoration: "none",
              overflow: "hidden",
              textOverflow: "ellipsis",
            }}
          >
            {name}
          </RouterLink>
        );
      },
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

  const handlePageChange = (newPage) => {
    setCurrentPage(newPage);
  };

  return (
    <DashboardLayout>
      <DashboardNavbar />
      <Box pt={6} pb={3}>
        <ToastContainer />
        <Header title="TAOBAO" subtitle="List Data" />
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
              backgroundColor: theme.palette.info.light,
              color: "white!important",
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
            {/* ... (Search bar and button) */}
          </Grid>
          <DataGrid
            getRowId={(row) => row.id}
            columns={columns}
            rows={data}
            checkboxSelection
            disableRowSelectionOnClick
            initialState={{
              ...data.initialState,
              pagination: { paginationModel: { pageSize: 5 } },
            }}
            pageSizeOptions={[5, 10, 25]}
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
      </Box>
      <Footer />
    </DashboardLayout>
  );
}

export default ListData;
