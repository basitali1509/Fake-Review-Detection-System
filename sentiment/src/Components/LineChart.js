import React from 'react';
import { Card, CardBody, Typography } from '@material-tailwind/react';
import Chart from 'react-apexcharts';



export default function PieChart({postiveCount,negativeCount,neutralCount}) {

  const pieChartConfig = {
    type: 'pie',
    height: 380,
    series: [postiveCount,negativeCount,neutralCount],
    options: {
      labels: ['Postive', 'Negative', 'Neutral'],
      colors: ['#549C30', '#B81B0E', '#F7B500'],
      legend: {
        labels: {
          colors: '#fff',
          useSeriesColors: false,
        },
      },
      tooltip: {
        theme: 'light',
      },
    },
  };
  return (
    <Card className="bg-[#323262] text-cyan-50">
      <CardBody className="px-2 pb-0">
        <Typography
          variant="h5"
          className="ml-4 self-center sm:self-start font-semibold text-cyan-50"
        >
          Sentiment From Data
        </Typography>
        <Chart {...pieChartConfig} />
      </CardBody>
    </Card>
  );
}
