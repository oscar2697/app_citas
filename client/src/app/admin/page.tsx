"use client";

import { useEffect, useState } from "react";
import StatCard from "@/components/StatCard";
import { columns } from "@/components/table/columns";
import { DataTable } from "@/components/table/DataTable";
import { getRecentAppointmentsList } from "@/lib/actions/appointment.actions";
import Image from "next/image";
import Link from "next/link";

const Admin = () => {
    const [appointments, setAppointments] = useState({
        scheduledCount: 0,
        pendingCount: 0,
        cancelledCount: 0,
        documents: [],
    });

    useEffect(() => {
        async function fetchAppointments() {
            try {
                const data = await getRecentAppointmentsList();
                setAppointments(data);
            } catch (error) {
                console.error("Error fetching appointments:", error);
            }
        }

        fetchAppointments();

        const interval = setInterval(fetchAppointments, 5000); 

        return () => clearInterval(interval); 
    }, []);

    return (
        <div className="mx-auto flex max-w-7xl flex-col space-y-14">
            <header className="admin-header">
                <Link href="/" className="cursor-pointer">
                    <Image
                        src="/assets/icons/danymed.png"
                        height={160}
                        width={810}
                        alt="Logo"
                        className="h-40 w-fit"
                    />
                </Link>

                <p className="text-16-semibold">Admin Dashboard</p>
            </header>

            <main className="admin-main">
                <section className="w-full space-y-4">
                    <h1 className="header">Bienvenido 👋🏻</h1>
                    <p className="text-dark-700">Empieza tu día administrando las citas.</p>
                </section>

                <section className="admin-stat">
                    <StatCard
                        type="appointments"
                        count={appointments.scheduledCount}
                        label="Citas Agendadas"
                        icon="/assets/icons/appointments.svg"
                    />

                    <StatCard
                        type="pending"
                        count={appointments.pendingCount}
                        label="Citas Pendientes"
                        icon="/assets/icons/pending.svg"
                    />

                    <StatCard
                        type="cancelled"
                        count={appointments.cancelledCount}
                        label="Citas Canceladas"
                        icon="/assets/icons/cancelled.svg"
                    />
                </section>

                <DataTable columns={columns} data={appointments.documents} />
            </main>
        </div>
    );
};

export default Admin;
